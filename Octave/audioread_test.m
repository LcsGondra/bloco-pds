[signal,fa]=audioread('Teste.wav');
plot(signal);
player=audioplayer(signal, fa);
##play(player);
fa;
myfft(signal,fa);
