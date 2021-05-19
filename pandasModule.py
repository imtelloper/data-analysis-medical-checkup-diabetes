import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class pandasModule:
    # 전체 걸럼의 unique값과 갯수를 찍어보자
    def showUniqueInfos(df):
        cols = df.columns
        for col in cols:
            print("#########" + str(col) + "#########")
            print(df[col].value_counts())
            print('\n')

    # 필요없는 혹은 이상치가 너무 많은 못쓰는 컬럼 삭제
    # ex) df = dropColum(df, [ 'payer_code', 'encounter_id'])
    def dropColum(df, column):
        dropedDf = df.drop(column, axis='columns')
        return dropedDf

    # 행 삭제
    def deleteRow(df, colName, val):
        indexNames = df[df[colName] == val].index
        # Delete these row indexes from dataFrame
        df.drop(indexNames, inplace=True)
        print(df[colName].value_counts())

    def oneHotEncod(df, columnName):
        df = pd.get_dummies(df, columns=[columnName])

    def showBoxPlots(df, xVal):
        cols = df.columns
        for col in cols:
            sns.boxplot(x=xVal, y=str(col), data=df)
            plt.show()
