# commands:

hjs -D mapred.reduce.tasks=1 -file src/ -mapper src/pr_mapper.sh -reducer src/pr_reducer.sh -input input.txt -output pr.out