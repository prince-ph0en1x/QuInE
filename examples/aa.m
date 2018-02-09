close all
clear all
clc

n = 5;

%% Grover
%
%	% Initialization
%	s = 1/sqrt(2^n)*ones(1,2^n);
%	plot([0:2^n-1],s,'-b')
%	hold on
%
%	m = 2;
%	t = 1;
%	iter = floor(pi/(4*asin(1/sqrt(2^n))))
%
%	for i = 1:iter
%		% Mark
%		s(m) = -s(m);
%		% Diffuse
%		s = -s + 2*mean(s);
%		if i == floor(iter/2)
%			plot([0:2^n-1],s,'*m')
%		end
%		if i == iter
%			plot([0:2^n-1],s,'.r')
%		end
%	end
%	axis([0 2^n-1 -1 1])

%% BBHT multiple solns
%
%	% Initialization
%	s = 1/sqrt(2^n)*ones(1,2^n);
%	plot([0:2^n-1],s,'-b')
%	hold on
%
%	m = [2 10];
%	t = size(m,2);
%	iter = floor(pi/(4*asin(sqrt(t/(2^n)))))
%
%	for i = 1:iter
%		% Mark
%		for mi = 1:t
%			s(m(mi)) = -s(m(mi));
%		end
%		% Diffuse
%		s = -s + 2*mean(s);
%		if i == floor(iter/2)
%			plot([0:2^n-1],s,'*m')
%		end
%		if i == iter
%			plot([0:2^n-1],s,'.r')
%		end
%	end
%	axis([0 2^n-1 -1 1])

%% BBHT N/4 solns
%
%	% Initialization
%	s = 1/sqrt(2^n)*ones(1,2^n);
%	plot([0:2^n-1],s,'-b')
%	hold on
%
%	m = [1:2^(n-2)];
%	t = size(m,2);
%	th = asin(sqrt(t/(2^n)));
%	iter = floor(pi/(4*th))
%	km = sin(th*((pi-2*th)/(2*th)+1))/sqrt(t)
%	lm = cos(3*th)/sqrt(2^n-t)
%
%	for i = 1:iter
%		% Mark
%		for mi = 1:t
%			s(m(mi)) = -s(m(mi));
%		end
%		% Diffuse
%		s = -s + 2*mean(s);
%		if i == floor(iter/2)
%			plot([0:2^n-1],s,'*m')
%		end
%		if i == iter
%			plot([0:2^n-1],s,'.r')
%			s(1)
%			s(2^n - 1)
%		end
%	end
%	axis([0 2^n-1 -1 1])

%% BBHT multiple unknown [1,3N/4] solns  ########### INCOMPLETE
%
%		% Initialization
%		N = 2^n
%		
%		%t = floor(rand*N + 1)
%		m = [2 10];
%		t = size(m,2);
%		
%		g = 6/5;
%		iterMax = 1;
%		
%		s = 1/sqrt(N)*ones(1,N);	% initial equal superposition
%		plot([0:N-1],s,'-b')
%		hold on
%		
%		
%		th = asin(sqrt(t/N))
%		m0 = 1/sin(2*th)
%		loopMax = ceil(log(m0)/log(g))
%		iterExpc = 
%		
%		
%		iterMax = min(g*iterMax,sqrt(N))
%		iterMax = min(g*iterMax,sqrt(N))
%		iterMax = min(g*iterMax,sqrt(N))
%		iterMax = min(g*iterMax,sqrt(N))
%		iterMax = min(g*iterMax,sqrt(N))
%		iterMax = min(g*iterMax,sqrt(N))
%		iter = floor(rand*iterMax)
%		
%	%	for i = 1:iter
%	%		% Mark
%	%		for mi = 1:t
%	%			s(m(mi)) = -s(m(mi));
%	%		end
%	%		% Diffuse
%	%		s = -s + 2*mean(s);
%	%		if i == floor(iter/2)
%	%			plot([0:2^n-1],s,'*m')
%	%		end
%	%		if i == iter
%	%			plot([0:2^n-1],s,'.r')
%	%		end
%	%	end
%		axis([0 2^n-1 -1 1])

%% Arbitrary initial amplitudes 1 soln
%
%	% Initialization
%	N = 2^n;
%	s = [ones(1,n)/sqrt(n) zeros(1,N-n)];
%	plot([0:N-1],s,'.-b')
%	hold on
%
%	r = 1
%	kavg = 1/sqrt(n)
%	lavg = (n-r)/((N-r)*sqrt(n))
%	lvar = sum((s(r+1:N) - lavg).^2)/(N-r);
%	Pmax = 1-(N-r)*lvar
%	%1-sum((s(r+1:N) - lavg).^2)
%	j = 5
%	T = ((j+0.5)*pi - atan(kavg*sqrt(r/(N-r))/lavg))/acos(1-2*r/N)
%	T = round(T);
%
%	for iter = 1:T
%		C = 2*((N-r)*lavg - r*kavg)/N;
%		%pred = [C+s(1) C-s(2:end)];
%		s(1) = -s(1);			% Mark
%		s = -s + 2*mean(s);		% Diffuse
%		%sum(abs(s-pred)) < 1e-14
%		kavg = C+kavg;
%		lavg = C-lavg;
%	end
%	disp(sprintf('\nIteration %d',T))
%	kavg
%	lavg
%	Pans = kavg^2
%	plot([0:2^n-1],s,'.-m')
%	axis([0 2^n-1 -1 1])
%
%	%	N;
%	%	M = 2;
%	%	r = 1;
%	%	iMx = N-M+1;
%	%	s = log2(iMx);
%	%	qb = s*M;
%	%	l0avg = (iMx - r)/((2^qb - r)*sqrt(iMx))
%	%	PmaxGene = 1 - (iMx - r)*(1/sqrt(iMx) - l0avg)^2 - (2^qb - iMx)*l0avg^2

%% Arbitrary initial amplitudes r solns
%
%	% Initialization
%	N = 2^n;
%	s = [ones(1,n)/sqrt(n) zeros(1,N-n)];
%	plot([0:N-1],s,'.-b')
%	hold on
%
%	r = 2
%	kavg = 1/sqrt(n)
%	lavg = (n-r)/((N-r)*sqrt(n))
%	lvar = sum((s(r+1:N) - lavg).^2)/(N-r);
%	Pmax = 1-(N-r)*lvar
%	%1-sum((s(r+1:N) - lavg).^2)
%	j = 1
%	T = ((j+0.5)*pi - atan(kavg*sqrt(r/(N-r))/lavg))/acos(1-2*r/N)
%	T = round(T);
%
%	for iter = 1:T
%		C = 2*((N-r)*lavg - r*kavg)/N;
%		%pred = [C+s(1) C-s(2:end)];
%		s(1:r) = -s(1:r);		% Mark
%		s = -s + 2*mean(s);		% Diffuse
%		%sum(abs(s-pred)) < 1e-14
%		kavg = C+kavg;
%		lavg = C-lavg;
%	end
%	disp(sprintf('\nIteration %d',T))
%	kavg
%	lavg
%	Pans = r*kavg^2
%	plot([0:2^n-1],s,'.-m')
%	axis([0 2^n-1 -1 1])

%% Hollenberg Iteration
%
%	A = 4;
%	M = 3;
%	N = 10;
%	r = 1;
%
%	iMx = N-M+1;
%	qtag = ceil(log2(iMx));
%	qb = qtag + M*ceil(log2(A));
%	sMx = 2^qb;
%
%	kavg0 = 1/sqrt(iMx);
%	lavg0 = (iMx - r)/((sMx - r)*sqrt(iMx));
%	Pmax = 1 - (sMx-iMx)*lavg0^2 - (iMx-r)*(1/sqrt(iMx) - lavg0)^2
%
%	j = [0:9]'
%	T = ((j+0.5)*pi - atan(kavg0*sqrt(r/(sMx-r))/lavg0))/acos(1-2*r/sMx)'

%% Panda Iteration

A = 2;
dim = 2;
M = 3;
N = 18;
r = 1;

iMx = (N-M+1)^dim
qtag = ceil(log2(iMx));
qb = qtag + M^dim*ceil(log2(A));
sMx = 2^qb;

kavg0 = 1/sqrt(iMx);
lavg0 = (iMx - r)/((sMx - r)*sqrt(iMx));
Pmax = 1 - (sMx-iMx)*lavg0^2 - (iMx-r)*(1/sqrt(iMx) - lavg0)^2

j = [0:9]'
T = ((j+0.5)*pi - atan(kavg0*sqrt(r/(sMx-r))/lavg0))/acos(1-2*r/sMx)'