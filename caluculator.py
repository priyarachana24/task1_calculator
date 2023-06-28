<!DOCTYPE html>
<html>
  <head>
    <script
      src="https://cdnjs.cloudflare.com/ajax/libs/mathjs/10.6.4/math.js"
      integrity="sha512-BbVEDjbqdN3Eow8+empLMrJlxXRj5nEitiCAK5A1pUr66+jLVejo3PmjIaucRnjlB0P9R3rBUs3g5jXc8ti+fQ=="
      crossorigin="anonymous"
      referrerpolicy="no-referrer"
    ></script>
    <script
      src="https://cdnjs.cloudflare.com/ajax/libs/mathjs/10.6.4/math.min.js"
      integrity="sha512-iphNRh6dPbeuPGIrQbCdbBF/qcqadKWLa35YPVfMZMHBSI6PLJh1om2xCTWhpVpmUyb4IvVS9iYnnYMkleVXLA=="
      crossorigin="anonymous"
      referrerpolicy="no-referrer"
    ></script>
    <!-- for styling -->
    <style>
      @font-face {
        font-family: PlusJakartaText-Regular;
        src: url("PlusJakartaText-Regular.otf");
      }

      * {
        font-family: PlusJakartaText-Regular;
      }

      body {
        background: #967bb6;
        text-align: center;
      }

      .container {
        background: white;
        border-radius: 25px;
        align-items: center;
        margin: 3vw;
        /*box-shadow: rgba(17, 12, 46, 0.15) 0px 48px 100px 0px;*/
        box-shadow: rgba(17, 12, 46, 0.15) 0px 48px 100px 0px;
      }

      label {
        font-size: 20px;
        font-weight: bold;
        width: 90px;
        display: inline-block;
        text-align: center;
      }

      table {
        margin-left: auto;
        margin-right: auto;
        border: 5px solid pink;
        margin-left: 30%;
        border-radius: 5%;
        background: rgb(185, 255, 170);
        background: linear-gradient(
          90deg,
          rgba(185, 255, 170, 1) 3%,
          rgba(133, 225, 219, 1) 46%,
          rgba(236, 179, 227, 1) 100%
        );
      }

      input[type="button"] {
        width: 100%;
        padding: 20px 40px;
        background-color: black;
        color: white;
        font-size: 24px;
        font-weight: bold;
        border: none;
        border-radius: 50%;
      }
      input:focus {
        outline: 2px solid #967bb6;
      }

      button {
        padding: 20px 70px;
        outline: none;
        margin: 40px;
        background-color: rgb(225, 133, 133);
        border-style: none;
        color: white;
        font-size: 20px;
        border-radius: 10px;
        transition-duration: 0.8s;
        cursor: pointer;
        font-size: 20px;
        font-weight: bold;
      }

      button:hover {
        background-color: #d4c7e4;
      }
      #table-box {
        margin: 0 20px;
        background-color: rgb(200, 255, 127);
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: left;
        border-radius: 20px;
        height: 500px;
        width: 800px;
        box-shadow: rgba(50, 50, 93, 0.25) 0px 6px 12px -2px,
          rgba(0, 0, 0, 0.3) 0px 3px 7px -3px;
      }
      #agree {
        padding-left: 20px;
        padding-top: 20px;
        font-size: 16px;
      }
      #agree input {
        margin-top: 10px;
        width: 20px;
        height: 20px;
        border: 1px solid #ccc;
        border-radius: 4px;
      }
      table-box {
        margin: 0 20px;
        background-color: #d4c7e4;
        justify-content: flex-start;
        align-items: center;
        border-radius: 20px;
        height: 500px;
        width: 800px;
      }

      td,
      th {
        padding-left: 10px;
        width: 100px;
        text-align: left;
      }

      input[type="text"] {
        padding: 20px 30px;
        background: rgb(225, 133, 133);
        background: linear-gradient(
          90deg,
          rgba(225, 133, 133, 1) 0%,
          rgba(232, 78, 208, 1) 37%,
          rgba(118, 187, 201, 1) 100%
        );
        font-size: 24px;
        font-weight: bold;
        border: none;
        color: white;
        border-radius: 20px;
        border: 3px solid purple;
      }
    </style>
  </head>
  <!-- create table -->

  <body>
    <table id="calcu">
      <tr>
        <td colspan="3"><input type="text" id="result" /></td>
        <!-- clr() function will call clr to clear all value -->
        <td>
          <input
            style="color: purple; background-color: whitesmoke"
            type="button"
            value="c"
            onclick="clr()"
          />
        </td>
      </tr>
      <tr>
        <!-- create button and assign value to each button -->
        <!-- dis("1") will call function dis to display value -->
        <td>
          <input
            type="button"
            value="1"
            onclick="dis('1')"
            onkeydown="myFunction(event)"
          />
        </td>
        <td>
          <input
            type="button"
            value="2"
            onclick="dis('2')"
            onkeydown="myFunction(event)"
          />
        </td>
        <td>
          <input
            type="button"
            value="3"
            onclick="dis('3')"
            onkeydown="myFunction(event)"
          />
        </td>
        <td>
          <input
            style="color: purple; background-color: white"
            type="button"
            value="/"
            onclick="dis('/')"
            onkeydown="myFunction(event)"
          />
        </td>
      </tr>
      <tr>
        <td>
          <input
            type="button"
            value="4"
            onclick="dis('4')"
            onkeydown="myFunction(event)"
          />
        </td>
        <td>
          <input
            type="button"
            value="5"
            onclick="dis('5')"
            onkeydown="myFunction(event)"
          />
        </td>
        <td>
          <input
            type="button"
            value="6"
            onclick="dis('6')"
            onkeydown="myFunction(event)"
          />
        </td>
        <td>
          <input
            style="color: purple; background-color: whitesmoke"
            type="button"
            value="*"
            onclick="dis('*')"
            onkeydown="myFunction(event)"
          />
        </td>
      </tr>
      <tr>
        <td>
          <input
            type="button"
            value="7"
            onclick="dis('7')"
            onkeydown="myFunction(event)"
          />
        </td>
        <td>
          <input
            type="button"
            value="8"
            onclick="dis('8')"
            onkeydown="myFunction(event)"
          />
        </td>
        <td>
          <input
            type="button"
            value="9"
            onclick="dis('9')"
            onkeydown="myFunction(event)"
          />
        </td>
        <td>
          <input
            style="color: purple; background-color: whitesmoke"
            type="button"
            value="-"
            onclick="dis('-')"
            onkeydown="myFunction(event)"
          />
        </td>
      </tr>
      <tr>
        <td>
          <input
            type="button"
            value="0"
            onclick="dis('0')"
            onkeydown="myFunction(event)"
          />
        </td>
        <td>
          <input
            style="color: purple; background-color: whitesmoke"
            type="button"
            value="."
            onclick="dis('.')"
            onkeydown="myFunction(event)"
          />
        </td>
        <!-- solve function call function solve to evaluate value -->
        <td>
          <input
            style="color: purple; background-color: whitesmoke"
            type="button"
            value="="
            onclick="solve()"
          />
        </td>

        <td>
          <input
            style="color: purple; background-color: whitesmoke"
            type="button"
            value="+"
            onclick="dis('+')"
            onkeydown="myFunction(event)"
          />
        </td>
      </tr>
    </table>
    <script>
      // Function that display value
      function dis(val) {
        document.getElementById("result").value += val;
      }

      function myFunction(event) {
        if (
          event.key == "0" ||
          event.key == "1" ||
          event.key == "2" ||
          event.key == "3" ||
          event.key == "4" ||
          event.key == "5" ||
          event.key == "6" ||
          event.key == "7" ||
          event.key == "8" ||
          event.key == "9" ||
          event.key == "+" ||
          event.key == "-" ||
          event.key == "*" ||
          event.key == "/"
        )
          document.getElementById("result").value += event.key;
      }

      var cal = document.getElementById("calcu");
      cal.onkeyup = function (event) {
        if (event.keyCode === 13) {
          console.log("Enter");
          let x = document.getElementById("result").value;
          console.log(x);
          solve();
        }
      };

      // Function that evaluates the digit and return result
      function solve() {
        let x = document.getElementById("result").value;
        let y = math.evaluate(x);
        document.getElementById("result").value = y;
      }

      // Function that clear the display
      function clr() {
        document.getElementById("result").value = "";
      }
    </script>
  </body>
</html>
