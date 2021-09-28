# Passing the current path to a file

When creating a file in batch using echo, it may be useful to pass the current directoy. This can be done with the following command:

```conda
> echo "%cd%" >> <file_name.type>
```

-   This could be used to immediately pass the PATH into a file a variable that can be operated on during the script
-   An example is below. I passed this into the file before I added the markdown text

```conda
"# C:\Users\mattr\OneDrive\Desktop\AFIT\Tab 1 - Current Semester\EENG_032_Python\read_data_pandas"
```
