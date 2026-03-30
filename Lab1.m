%% Parámetros iniciales de la simulación
fc = 1000;              % Frecuencia de la señal original (Hz)
fs = 8000;              % Frecuencia de muestreo (Hz) - Debe ser > 2*fc
fs_sim = 100000;        % Frecuencia de simulación (alta para simular tiempo continuo)
t_end = 0.005;          % Tiempo total de simulación (5 ms para ver varios ciclos)
t = 0:1/fs_sim:t_end;   % Vector de tiempo continuo››
duty_cycle = 50;        % Ciclo de trabajo de los pulsos (%)

%% 1. Actividades Previas: Señales en el tiempo
% Generación de la señal original
m_t = sin(2 * pi * fc * t); % Con fc en 1000hz

% Generación del tren de pulsos
tren_pulsos = (square(2 * pi * fs * t, duty_cycle) + 1) / 2;

% PAM Natural
pam_natural = m_t .* tren_pulsos;

% PAM Instantánea (Sample and Hold)
t_muestras = 0:1/fs:t_end;                     % Instantes de muestreo
m_muestras = sin(2 * pi * fc * t_muestras);    % Valores muestreados
% Retención de orden cero (interp1 con 'previous')
pam_inst_retencion = interp1(t_muestras, m_muestras, t, 'previous'); 
% Aplicar el ancho de pulso
pam_instantanea = pam_inst_retencion .* tren_pulsos;

% Gráfica en el dominio del tiempo
figure('Name', 'Señales en el Tiempo', 'NumberTitle', 'off');
subplot(3,1,1);
plot(t*1000, m_t, 'b', 'LineWidth', 1.5);
title('Señal Original m(t)'); xlabel('Tiempo (ms)'); ylabel('Amplitud'); grid on;

subplot(3,1,2);
plot(t*1000, pam_natural, 'r', 'LineWidth', 1.5);
title('Señal PAM Natural'); xlabel('Tiempo (ms)'); ylabel('Amplitud'); grid on;

subplot(3,1,3);
plot(t*1000, pam_instantanea, 'k', 'LineWidth', 1.5);
title('Señal PAM Instantánea'); xlabel('Tiempo (ms)'); ylabel('Amplitud'); grid on;

%% 2. Actividades: Transformada de Fourier (FFT)
N_fft = length(t);
f = linspace(-fs_sim/2, fs_sim/2, N_fft);

% Cálculo de las FFT centradas
M_f = abs(fftshift(fft(m_t))) / N_fft;
PAM_nat_f = abs(fftshift(fft(pam_natural))) / N_fft;
PAM_inst_f = abs(fftshift(fft(pam_instantanea))) / N_fft;

% Gráfica en el dominio de la frecuencia
figure('Name', 'Espectro de Frecuencias (FFT)', 'NumberTitle', 'off');
subplot(3,1,1);
plot(f, M_f, 'b', 'LineWidth', 1.5);
title('Espectro de la Señal Original'); xlabel('Frecuencia (Hz)'); ylabel('Magnitud'); 
xlim([-15000 15000]); grid on;

subplot(3,1,2);
plot(f, PAM_nat_f, 'r', 'LineWidth', 1.5);
title('Espectro PAM Natural'); xlabel('Frecuencia (Hz)'); ylabel('Magnitud'); 
xlim([-15000 15000]); grid on;

subplot(3,1,3);
plot(f, PAM_inst_f, 'k', 'LineWidth', 1.5);
title('Espectro PAM Instantánea'); xlabel('Frecuencia (Hz)'); ylabel('Magnitud'); 
xlim([-15000 15000]); grid on;

%% 3. Modulación PCM y Error de Cuantización
N_bits = 3; % N es configurable (prueba cambiarlo a 8 para ver cómo se reduce el error)
L = 2^N_bits; % Número de niveles
Vmax = 1;
Vmin = -1;
delta = (Vmax - Vmin) / L; % Tamaño del escalón

% Cuantificación de la señal PAM instantánea
% Usamos round para aproximar al nivel más cercano
pam_cuantificada = round(pam_instantanea / delta) * delta;

% Cálculo del error de cuantización
error_cuantizacion = pam_instantanea - pam_cuantificada;

% Gráfica de PCM
figure('Name', 'Modulación PCM y Cuantización', 'NumberTitle', 'off');
subplot(2,1,1);
hold on;
plot(t*1000, m_t, 'b--', 'LineWidth', 1);
plot(t*1000, pam_instantanea, 'k', 'LineWidth', 1.2);
plot(t*1000, pam_cuantificada, 'r', 'LineWidth', 1.5);
title(['Modulación PCM con N = ', num2str(N_bits), ' bits']);
legend('Original', 'PAM Inst', 'Cuantificada');
xlabel('Tiempo (ms)'); ylabel('Amplitud'); grid on; hold off;

% Gráfica del error de cuantización
subplot(2,1,2);
plot(t*1000, error_cuantizacion, 'm', 'LineWidth', 1.2);
title('Error de Cuantización'); xlabel('Tiempo (ms)'); ylabel('Amplitud del Error'); grid on;
