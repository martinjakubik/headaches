data = csvread('/Users/martin/code/gitwork/headaches/data-preparation/resources/data1-generated-negatives-auto.txt');

X = data(:, 1:9); y = data(:, 10);
m = length(y); % number of training examples

% Print out some data points
fprintf('Some 10 examples from the dataset: \n');
fprintf(' x = [%.0f %.0f %.0f %.0f %.0f %.0f %.0f %.0f %.0f], y = %.0f \n', [X(120:130,:) y(120:130,:)]');

fprintf('Program paused. Press enter to continue.\n');
pause;

% Plot Data
% Note: You have to complete the code in plotData.m
plotData(X, y);

fprintf('Program paused. Press enter to continue.\n');
pause;
