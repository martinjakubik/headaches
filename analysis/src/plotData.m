function plotData(x, y)

% opens a new figure window
figure;

% plots the data
plot(x, y, 'rx', 'MarkerSize', 4);

% sets the y-axis label
ylabel('Is headache?');

% sets the x-axis label
xlabel('Date');
