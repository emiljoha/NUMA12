%Data definition
xi = [0 1 2 3 4 5 6];
fx = [-35 -56 0 -16 -3 4 10];

%Sets Z and not Z
vectorZ = [];
compZ = [];

%Construction of Z and not Z
for k = 1:7
    for t = 1:7
        if xi(t)~=xi(k)
            Z = [xi(k) xi(t)];
            compZ = [compZ; setxor(0:6,Z)];
            vectorZ = [vectorZ; Z];
        end
    end
end

alerrors = []; %here goes the summed error for each set Z

for k = 1:size(vectorZ)
    errorvector = []; %vector for each one of the K errors
    A = [vectorZ(k,1) 1;vectorZ(k,2) 1];
    b = [fx(vectorZ(k,1)+1) fx(vectorZ(k,2)+1)]';
    sol = A\b;
    for t = 1:5
        error = abs(fx(compZ(k,t)+1)-(sol(1)*compZ(k,t)+compZ(k,t)));
        errorvector = [errorvector error];
    end
    erroratk = sum(errorvector); %sum at iteration K
    alerrors = [alerrors, erroratk]; %vector of which we want the min
end

[num,argnum] = min(alerrors);

%construction of the solution
A = [vectorZ(argnum,1) 1;vectorZ(argnum,2) 1];
b = [fx(vectorZ(argnum,1)+1) fx(vectorZ(argnum,2)+1)]';
sol = A\b;

polynom = sol(1)*xi+sol(2);

figure
plot(xi,fx,'*')
hold on
plot(xi,polynom)
hold off