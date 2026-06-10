from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import os

app = Flask(__name__)

data_file = os.path.join(os.path.dirname(__file__), 'static', 'global_education_data.csv')
df = pd.read_csv(data_file)

@app.route('/')
def index():
    # Out-of-School Rates
    oosr_cols = ["OOSR_Primary_Age_Male", "OOSR_Primary_Age_Female", "OOSR_Lower_Secondary_Age_Male", "OOSR_Lower_Secondary_Age_Female"]
    oosr_df = df.melt(id_vars=["Countries and areas"], value_vars=oosr_cols, var_name="Category", value_name="Rate")
    fig_oosr = px.bar(oosr_df, x="Countries and areas", y="Rate", color="Category", title="Out-of-School Rates by Country")
    oosr_graph = fig_oosr.to_html()

    # Literacy Rates
    literacy_df = df[["Countries and areas", "Youth_15_24_Literacy_Rate_Male", "Youth_15_24_Literacy_Rate_Female"]]
    fig_lit = px.bar(literacy_df.melt(id_vars=["Countries and areas"], var_name="Gender", value_name="Literacy Rate"), 
                      x="Countries and areas", y="Literacy Rate", color="Gender", title="Youth Literacy Rates (15-24)")
    literacy_graph = fig_lit.to_html()

    # Completion Rates
    completion_cols = ["Completion_Rate_Primary_Male", "Completion_Rate_Primary_Female", "Completion_Rate_Lower_Secondary_Age_Male", "Completion_Rate_Lower_Secondary_Age_Female"]
    completion_df = df.melt(id_vars=["Countries and areas"], value_vars=completion_cols, var_name="Category", value_name="Rate")
    fig_completion = px.bar(completion_df, x="Countries and areas", y="Rate", color="Category", title="Completion Rates by Country")
    completion_graph = fig_completion.to_html()

    # Enrollment Rates
    enrollment_df = df[["Countries and areas", "Gross_Primary_Education_Enrollment", "Gross_Tertiary_Education_Enrollment"]]
    fig_enroll = px.bar(enrollment_df.melt(id_vars=["Countries and areas"], var_name="Level", value_name="Enrollment Rate"), 
                         x="Countries and areas", y="Enrollment Rate", color="Level", title="Enrollment Rates")
    enrollment_graph = fig_enroll.to_html()
    
    # Birth Rate vs Education Indicators
    fig_birth = px.scatter(df, x="Birth_Rate", y="Gross_Primary_Education_Enrollment", size="Gross_Tertiary_Education_Enrollment", 
                           color="Countries and areas", title="Birth Rate vs. Education Enrollment")
    birth_graph = fig_birth.to_html()
    
    return render_template("index.html", oosr_graph=oosr_graph, literacy_graph=literacy_graph, 
                           completion_graph=completion_graph, enrollment_graph=enrollment_graph, birth_graph=birth_graph)

if __name__ == '__main__':
    app.run(debug=True)
