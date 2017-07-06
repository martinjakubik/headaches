function plotData(X, y)

% opens a new figure window
figure; hold on;

pos = find(y==1);
neg = find(y==0);

% plots the data
plot(X(neg, 2), X(neg, 4), 'ko', 'MarkerSize', 2);
plot(X(pos, 2), X(pos, 4), 'kx', 'MarkerSize', 8, 'MarkerFaceColor', 'r');


% sets the y-axis label
ylabel('Day of the week');

% sets the x-axis label
xlabel('Date');
