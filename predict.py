from clean import clean
from sklearn.preprocessing import MinMaxScaler
from sklearn.tree import DecisionTreeClassifier
import pandas as pd



df = clean('train.csv')
dfTest = clean('test.csv')
ids = dfTest.PassengerId
x = df.drop(['PassengerId','Transported'],axis=1)
x2 = dfTest.drop(['PassengerId'],axis=1)
y_train= df['Transported']

scaler=MinMaxScaler()
scaler.fit(x)

x_train_transformada=scaler.transform(x)
x_test_transformada=scaler.transform(x2)

def DTree():
    model_t=DecisionTreeClassifier(random_state=10)
    model_t.fit(x_train_transformada,y_train)

    y_hat_t=model_t.predict(x_test_transformada)
    return y_hat_t



def concatenar(ids,emission,name):
    final=pd.DataFrame()
    final['PassengerId'] = ids['PassengerId']
    final['Transported']=pd.Series(emission)
    final['Transported']=final['Transported']
    final.to_csv(name,index=False)
    print("checa tu csv con nombre: "+name)
    return final


if __name__=='__main__':
    DT = DTree()
    concatenar(dfTest,DT,'DT.csv')




