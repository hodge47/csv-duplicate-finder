# csv-duplicate-finder
A Python script to find duplicates across multiple csv files and compile results into an output csv files

<br>

## Usage
<ol>
  <li> Move <code>duplicate-finder.py</code> into a new folder somwhere of your choosing.</li>
  <li> Create a folder called `csv` in the same directory as `duplicate-finder.py`.</li>
  <li> Move your csv files into the `csv` folder.</li>
  <li> Run the Python script:</li>
  <ol>
    <li> `python3 duplicate-finder.py [csv folder] [files in folder]`</li>
    Example: `python3 duplicate-finder.py csv one.csv two.csv three.csv`
  </ol>
</ol>

If there are any duplicate entries, a folder called `Output` will be created in thee same directory as `duplicate-finder.py` containing a csv file of all duplicates and their combineed data.
