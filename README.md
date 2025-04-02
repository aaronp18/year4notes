# Year 4 Notes

## Generating Tables
Instead of revising, I've spent time developing a script that collates all of the equations in a document and puts them in a nice neat table :)

To install:
```bash
cd scripts
npm install
npm install -g  markdown-table-formatter
```

- Add to the top of your md file the tag. The script will replace whatever is in between the tags with the table.
```markdown
<equation-table>
</equation-table>
```

 To add equations to the files simply make a equations div for each category followed by a `##` with the name of the category.
 Below that, you then can add the equation title (#### Title), followed by a description (optional) with the equation after that in
 double dollar signs ($$ equation $$). Anything after that is ignored. If there is no double dollar signs (no big equations, then it
  will add the first 80 characters (see const characterLimit)).
 
 Then to add the equation table, simply add a <equation-table></equation-table> tag. This is then replaced every time this is run. 
 Also only ever add 1 of these, otherwise it will get replaced.
 
 Then simply run the generateTables.sh file at the root of the project.
 
 Change character limit (default 60) to the number of characters to print in the table when using simple text.
 
 EG: 
 ```
 <equation-table></equation-table>
 
 <div class="equations">

 ## Capacitors

 ### Energy Stored
 
 The energy stored by a capacitor of capacitance, C with a voltage, v
 $$ E = \frac{1}{2} C V^2$$
 
 - $C$ = Capacitance, Farads, F
 - $V$ = Voltage, Volts, V
 
 ### Just text
 
 This here is an explantation that will be added, as long as there are no double dollar equations
   
 </div>
 ```

Then run:
```bash
cd scripts
./generate_tables.sh ../src
```
