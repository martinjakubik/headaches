function plotData(X, y)

% opens a new figure window
figure; hold on;

pos = find(y==1);
neg = find(y==0);

numWeekdays = sum(X(pos, 4) == (0:6));

bar(numWeekdays);

% sets the y-axis label
xlabel('Day of the week');

% sets the x-axis label
ylabel('Number of headaches');

% opens a new figure window
figure; hold on;

numMonths = sum(X(pos, 2) == (1:12));

bar(numMonths);

% opens a new figure window
figure; hold on;

numMonthDays = sum(X(pos, 3) == (1:31));

bar(numMonthDays);
