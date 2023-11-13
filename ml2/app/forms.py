from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField


from wtforms.validators import NumberRange, DataRequired



class inputfield(FlaskForm):

    YearBuilt=IntegerField('What year was your house built?', validators=[DataRequired()])

    YearRemodAdd=IntegerField('If your house was remodeled, what year was this? (If no, input year built).', validators=[DataRequired()])

    GrLivArea=IntegerField('How many square feet is your ground living area?', validators=[DataRequired()])

    TotalBsmtSF=IntegerField('How many square feet is your basement?', validators=[DataRequired()])

    FirstFlrSF=IntegerField('How many square feet is your first floor?', validators=[DataRequired()])

    TotRmsAbvGrd=IntegerField('How many rooms above ground do you have in your house?', validators=[DataRequired()])

    FullBath=IntegerField('How many full bathrooms do you have in your house?', validators=[DataRequired()])

    
    
    OverallQual=IntegerField('What is your house qiality? Rate 1 through 10)',validators=[NumberRange(min=0,max=10)])
    
    #prøvde å få DataRequired her men fekk det ikkje til lole

   
    
    
    GarageArea=IntegerField('How many square feet of garage area?', validators=[DataRequired()])
    
    GarageCars=IntegerField('How many cars is the garage made for?', validators=[DataRequired()])
    
   

    submit = SubmitField('Submit')