import pandas as pd
import argparse

def main():
    parser = argparse.ArgumentParser(description='Add a gene column based on position ranges from another TSV file.')
    parser.add_argument('--inTSV', required=True, help='Path to the input TSV file')
    parser.add_argument('--geneTSV', required=True, help='Path to the gene information TSV file')
    parser.add_argument('--outTSV', required=True, help='Path to the output TSV file')
    args = parser.parse_args()

    # Read the input TSV file
    df_in = pd.read_csv(args.inTSV, sep='\t', header=None, names=['Sequence', 'Position', 'Value'])

    # Read the gene information TSV file
    df_gene = pd.read_csv(args.geneTSV, sep='\t')

    # Merge the two dataframes based on the position criteria
    merged_df = pd.merge_asof(df_in, df_gene, left_on='Position', right_on='Start', direction='backward')

    # Fill missing values in 'Gene' column with "Non-coding"
    merged_df['Gene'] = merged_df['Gene'].fillna('Non-coding')

    # Drop the "Start" and "End" columns
    merged_df = merged_df.drop(['Start', 'End'], axis=1)

    # Save the updated TSV file
    merged_df.to_csv(args.outTSV, sep='\t', index=False)
    print(f"Output saved to {args.outTSV}")

if __name__ == '__main__':
    main()
