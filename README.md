# csv-duplicate-finder
A Python script to find duplicates across multiple csv files and compile results into an output csv files

## Usage
<ol>
  <li> Move <code>duplicate-finder.py</code> into a new folder somwhere of your choosing.</li>
  <li> Create a folder called <code>csv</code in the same directory as <code>duplicate-finder.py</code>.</li>
  <li> Move your csv files into the <code>csv</code> folder.</li>
  <li> Run the Python script:</li>
  <ol>
    <li> <code>python3 duplicate-finder.py [csv folder] [files in folder]</code></li>
    Example: <code>python3 duplicate-finder.py csv one.csv two.csv three.csv</code>
  </ol>
</ol>

If there are any duplicate entries, a folder called <code>Output</code> will be created in thee same directory as <code>duplicate-finder.py</code> containing a csv file of all duplicates and their combineed data.
