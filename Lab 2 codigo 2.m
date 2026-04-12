%% Configuración de Parámetros (Actividad IV-A)
n_bits = 1e2;              % 10^4 bits solicitados
sps = 8;                   % Muestras por símbolo (Samples per symbol)
f0 = 1;                    % Frecuencia de corte a 6dB
Ts = 1/(2*f0);             % Tiempo de símbolo
alphas = [0, 0.25, 0.75, 1]; % Valores de roll-off de la actividad previa
snr = 20;                  % Relación Señal-Ruido (SNR) para el canal AWGN

%% 1. Generación de Bits y Codificación NRZ-L
bits = randi([0 1], n_bits, 1);
nrz_signal = 2*bits - 1;   % Convertir 0 a -1V y 1 a +1V

% Upsampling (insertar ceros entre símbolos para poder filtrar)
upsampled_signal = upsample(nrz_signal, sps);

figure('Name', 'Diagramas de Ojo - Filtro Coseno Alzado');

for i = 1:length(alphas)
    alpha = alphas(i);
    
    %% 2. Diseño del Filtro Coseno Alzado (Ecuación 14)
    % Usamos la función nativa de Matlab para diseño de filtros de comunicación
    span = 10;             % Extensión del filtro en símbolos
    h = rcosdesign(alpha, span, sps, 'sqrt'); % Filtro de raíz de coseno alzado
    
    %% 3. Filtrado y Canal con Ruido (AWGN)
    % Filtrar la señal
    tx_signal = filter(h, 1, upsampled_signal);
    
    % Agregar ruido blanco gaussiano
    rx_signal = awgn(tx_signal, snr, 'measured');
    
    %% 4. Visualización del Diagrama de Ojo
    subplot(2, 2, i);
    % Mostramos 2 periodos de símbolo para ver el "ojo" completo
    eyediagram(rx_signal(span*sps : end), 2*sps);
    title(['Diagrama de Ojo con \alpha = ', num2str(alpha)]);
end