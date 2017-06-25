data = csvread('/Users/martin/code/gitwork/headaches/data-preparation/resources/data1-generated-negatives-auto.txt');
X = data(:, 1); y = data(:, 2);
m = length(y); % number of training examples
