#flask sine esensielle bibloteker 
import flask
from flask import Flask, render_template, redirect, url_for, session
#esensielle bibloteker for bruk av databaser 
from sqlalchemy import create_engine,Column,String,Integer,CHAR,DateTime,delete
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import forms

import datetime
from datetime import time







#configurering og inisiering at denne appen er laget med flask og får egenskapene som følger med

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SECRET_KEY'] = 'Eliaserbosss'

Base = declarative_base()



#database klassen 
class Lekser(Base):
    __tablename__="lekser"
    id = Column("id",Integer,primary_key=True)
    frist = Column("frist",DateTime, nullable=False)
    oppgave=Column("oppgave",String(120),nullable=False)
    fag=Column("fag",String(60),nullable=False)


    
    


#initsierer kobling til db 
engine= create_engine("sqlite:///lekser.db",echo=True)
Base.metadata.create_all(bind=engine)
Session= sessionmaker(bind=engine)
session= Session()




@app.route('/')
def index():
    #lager en tom liste til hvert dataset som skal vises i 
    frist=[]
    oppgave=[]
    fag=[]
    
    #henter all dataen og setter det i rekkefølge etter dato 
    data=Session().query(Lekser).order_by(Lekser.frist)


    dato_i_dag =  datetime.datetime.today().date()
    dato_i_dag = datetime.datetime.combine(dato_i_dag, datetime.time(0, 0))

    for rad in data: 
        if rad.frist<dato_i_dag: 
            session.query(Lekser).filter_by(frist=rad.frist).delete()
            session.commit()

    
    for objekt in data:
        oppgave.append(objekt.oppgave)
        fag.append(objekt.fag)
        frist.append(str(objekt.frist))
       

    indexes=[*range(len(frist))]
    return render_template('index.html',frist=frist,oppgave=oppgave,indexes=indexes, fag=fag)


@app.route('/lag_lekse', methods=['GET','POST'])
def lag_lekse():
    lag_lekse_form=forms.Lekse_form()

    frist = lag_lekse_form.frist.data
    oppgave= lag_lekse_form.oppgave.data
    fag=lag_lekse_form.fag.data
    


    date = datetime.datetime.today().date()
    
    if flask.request.method == "POST":
        ny_lekse=Lekser(frist=frist,oppgave=oppgave, fag=fag)
        session.rollback()
        session.add(ny_lekse)
        session.commit()
        return redirect(url_for('index'))

    return render_template('lag_lekse.html',form=lag_lekse_form)

   


if __name__ == '__main__':
    app.run()