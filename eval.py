from sklearn.metrics import f1_score, precision_score, recall_score

def main():
    tags_true = []
    tags_pred = []

    correct_count = 0
    valid_line_count = 0

    for line in open("output.txt"):
        line = line.strip()
        if not line:
            continue
        _, tag_true, tag_pred = line.split()
        tags_true.append(tag_true)
        tags_pred.append(tag_pred)

        valid_line_count += 1
        if tag_true == tag_pred:
            correct_count += 1

    print(f'{correct_count} out of {valid_line_count} predictions are correct.')

    print(f'Precision: {precision_score(tags_true, tags_pred, average="macro")}\n'
          f'Recall: {recall_score(tags_true, tags_pred, average="macro")}\n'
          f'F1: {f1_score(tags_true, tags_pred, average="macro")}')

if __name__ == '__main__':
    main()