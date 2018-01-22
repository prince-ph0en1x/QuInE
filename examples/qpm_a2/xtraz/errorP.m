%((N!/(A*((N/A)!)))+(A^N-(N!/(A*((N/A)!))))/A)/(A^N)

figure(1)
hold on
er = zeros(1,15);

% N = 32;
% for A = 2:16
%     s = A^N;
%     f1 = factorial(N);
%     f2 = factorial(ceil(N/A));
%     t1 = f1/(f2^A);
%     er(A-1) = (t1 + (s - t1)/A)/s;
% end
% plot([2:16],er,'g')
% 
% N = 64;
% for A = 2:16
%     s = A^N;
%     f1 = factorial(N);
%     f2 = factorial(ceil(N/A));
%     t1 = f1/(f2^A);
%     er(A-1) = (t1 + (s - t1)/A)/s;
% end
% plot([2:16],er,'b')

N = 128;
for A = 2:16
    s = A^N;
    f1 = factorial(N);
    f2 = factorial(ceil(N/A));
    t1 = f1/(f2^A);
    er(A-1) = (t1 + (s - t1)/A)/s;
end
plot([2:16],er,'-or')

xlim([2 16])
ylim([0 1])
% title('Error fraction for different Alphabet size')
grid on
xlabel('Alphabet Size')
ylabel('Error Fraction')

