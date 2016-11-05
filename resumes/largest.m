figure(1)
x = 1:10;
y = x;
plot (x,y)

hold on

randIDXup = randperm(10,5);
randIDXdown = randperm(10,5);
yup = y(randIDXup)+ 0.25;

ydown = y(randIDXdown) -0.25;

y2pre = [yup ydown];
y2 = sort(y2pre);
plot(x,y2,'k*')
