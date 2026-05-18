fb = 1000;          % tasa de bits
t = 0:1e-5:5e-3;
m = square(2*pi*fb*t) * 0.5 + 0.5;  % onda cuadrada unipolar

% Transformada de Fourier
N = length(m);
f = linspace(-fb*7, fb*7, N);
G = abs(fftshift(fft(m)));

plot(f, G/max(G));
xlabel('Frecuencia (Hz)');
ylabel('|G(f)|');
title('Espectro de la envolvente compleja ASK');
saveas(gcf, 'miGrafico.png')