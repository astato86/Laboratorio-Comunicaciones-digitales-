%% actividad 1
% Parámetros de simulación
f0 = 1;                             % Ancho de banda a 6 dB 
Ts = 1 / (2*f0);                    % Tiempo de muestreo (Nyquist) 
alphas = [0, 0.25, 0.75, 1];        % Factores de roll-off 

% --- CAMBIO AQUÍ: Eje de tiempo de -4Ts a 4Ts para ver la simetría ---
t = -4*Ts : 0.001 : 4*Ts; 

% Definición del eje de frecuencia (-2B <= f <= 2B) B_max = f0 * (1 + max(alphas)); 
f = -2*B_max : 0.01 : 2*B_max;

figure('Color', 'w');

for i = 1:length(alphas)
    a = alphas(i);
    fd = a * f0;                    % f_delta 
    B = f0 + fd;                    % Ancho de banda absoluto 
    f1 = f0 - fd;                   % f1 
    
    % --- Respuesta al Impulso he(t) (Ecuación 14)  ---
    % Nota: sinc(x) en Matlab es sin(pi*x)/(pi*x)
    term1 = 2 * f0 * sinc(2 * f0 * t);
    term2 = cos(2 * pi * fd * t) ./ (1 - (4 * fd * t).^2);
    
    % Manejo del límite matemático (L'Hôpital) cuando el denominador es cero
    term2(abs(1 - (4 * fd * t).^2) < 1e-10) = pi/4; 
    he_t = term1 .* term2;
    
    % --- Respuesta en Frecuencia He(f) (Ecuación 10)  ---
    He_f = zeros(size(f));
    for j = 1:length(f)
        abs_f = abs(f(j));
        if abs_f <= f1
            He_f(j) = 1;
        elseif abs_f > f1 && abs_f <= B
            He_f(j) = 0.5 * (1 + cos((pi * (abs_f - f1)) / (2 * fd)));
        else
            He_f(j) = 0;
        end
    end
    
    % Gráfica en el Tiempo
    subplot(2,1,1);
    plot(t, he_t, 'LineWidth', 1.5, 'DisplayName', ['\alpha = ', num2str(a)]);
    hold on;
    
    % Gráfica en Frecuencia
    subplot(2,1,2);
    plot(f, He_f, 'LineWidth', 1.5, 'DisplayName', ['\alpha = ', num2str(a)]);
    hold on;
end

% Formato de Gráfica de Tiempo
subplot(2,1,1);
title('Respuesta al Impulso $h_e(t)$ (Simetría Completa)', 'Interpreter', 'latex');
xlabel('Tiempo (s)'); ylabel('Amplitud');
grid on; xline(0, '--k'); % Eje central
% Marcar puntos de muestreo n*Ts para verificar ISI cero 
xticks(-4*Ts : Ts : 4*Ts); 
legend;

% Formato de Gráfica de Frecuencia
subplot(2,1,2);
title('Respuesta en Frecuencia $H_e(f)$', 'Interpreter', 'latex');
xlabel('Frecuencia (Hz)'); ylabel('Magnitud');
grid on;
legend;
%% actividad 2

