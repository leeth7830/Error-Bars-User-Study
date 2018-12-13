from pandas import pandas as pd
import os

merged_output = "output/merged_output.csv"

input_path_one = "input/error_bars_1.csv"
output_path_one = "output/output1.csv"
worker_input_one = "input/G1-Batch_3451211_batch_results.csv"
worker_output_one = "output/workers1.csv"
graph_type_one = "bar"

input_path_two = "input/error_bars_2.csv"
output_path_two = "output/output2.csv"
worker_input_two = "input/G2-Batch_3451225_batch_results.csv"
worker_output_two = "output/workers2.csv"
graph_type_two = "box"

input_path_three = "input/error_bars_3.csv"
output_path_three= "output/output3.csv"
worker_input_three = "input/G3-Batch_3452500_batch_results.csv"
worker_output_three = "output/workers3.csv"
graph_type_three = "gradient"

input_path_four = "input/error_bars_4.csv"
output_path_four = "output/output4.csv"
worker_input_four = "input/G4-Batch_3452501_batch_results.csv"
worker_output_four = "output/workers4.csv"
graph_type_four = "violin"

def transform(input_path, output_path, worker_input, worker_path, graph_type):
    df = pd.read_csv(input_path, header=None)
    df = df.iloc[1:]
    columns = ['worker_id', 'question', 'response', 'answer', 'correct', 'confidence', 'likely']
    df2 = pd.DataFrame(columns=columns)
    for a, row in enumerate(df.values):
        response = None
        confidence = None
        likely = None
        worker_id = row[1]
        for i in range(2,110,1):
            if (i+1)%3 == 0:
                if row[i] == "Fewer votes":
                    response = 0
                else:
                    response = 1
            elif (i+1)%3 == 1:
                confidence = row[i]
            else:
                likely = row[i]
                question =  int(i/3)
                answer = None
                if (question+1)%2 == 0:
                    answer = 1 #more votes
                else:
                    answer = 0 #fewer votes
                correct = None
                if response == answer:
                    correct = 1
                else :
                    correct = 0
                df2.loc[((a)*36) + question - 1] = [worker_id, question, response, answer, correct, confidence, likely]
                df2 = df2.sort_index()

    if os.path.exists(output_path):
        os.remove(output_path)
    df2.to_csv(output_path)


    #Worker Report
    worker_stats = pd.read_csv(worker_input, index_col = 'WorkerId')
    worker_stats = worker_stats['WorkTimeInSeconds'].reset_index()
    worker_stats.columns = ['worker_id', 'WorkTimeInsecond']
    if os.path.exists(worker_path):
        os.remove(worker_path)
    df2['correct'] = pd.to_numeric(df2['correct'])
    df3 = df2.groupby('worker_id')['correct'].mean().reset_index()
    merged = pd.merge(df3, worker_stats, how = 'left', on = ['worker_id'])
    print(worker_path)
    print(merged.head())
    print()
    merged.to_csv(worker_path)

    #Merged Data
    df2['type'] = graph_type
    df2.to_csv(merged_output, mode='a', index = False, header= False)

if os.path.exists(merged_output):
    os.remove(merged_output)
transform(input_path_one, output_path_one, worker_input_one, worker_output_one, graph_type_one)
transform(input_path_two, output_path_two, worker_input_two, worker_output_two, graph_type_two)
transform(input_path_three, output_path_three, worker_input_three, worker_output_three, graph_type_three)
transform(input_path_four, output_path_four, worker_input_four, worker_output_four, graph_type_four)
#    print(df[df.columns[1]])
