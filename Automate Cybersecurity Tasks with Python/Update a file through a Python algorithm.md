# Algorithm for file updates in Python

## Project description

As a security professional, I am responsible for managing access to sensitive server content. This involves maintaining an "allow list" of IP addresses authorized to access specific restricted data. In this project, I developed a Python algorithm to automate the process of updating this allow list by removing unauthorized IP addresses stored in a separate "remove list." By automating this task, I ensure the security database remains accurate and reduce the risk of manual entry errors.

## Open the file that contains the allow list
To start the algorithm, I assigned the name of the file, `"allow_list.txt"`, to a variable named `import_file`. I then used a `with` statement to open the file securely.

```python
# Assign the file name to a variable
import_file = "allow_list.txt"

# Open the file using a 'with' statement
with open(import_file, "r") as file:
```

The `with` statement is used here because it ensures the file is automatically closed after the code block finishes, which helps prevent memory leaks. The `open()` function takes two arguments: the file variable and the `"r"` string, which indicates I am opening the file in **read** mode.

## Read the file contents
Once the file was open, I needed to extract the data into a format Python can manipulate. I used the `.read()` method to convert the file's contents into a single string.

```python
# Read the file and store it in a variable
ip_addresses = file.read()
```
The `.read()` method takes the text from the `file` object and stores it as a string in the new variable `ip_addresses`. This allows me to work with the data as a whole before breaking it down into individual components.


## Convert the string into a list
To remove individual IP addresses, I first needed to convert the long string into a list of separate elements. I achieved this using the `.split()` method.

```python
# Convert the string of IP addresses into a list
ip_addresses = ip_addresses.split()
```

By default, `.split()` separates a string into list items based on whitespace. This is ideal for this scenario as each IP address in the file is separated by spaces or new lines, turning the `ip_addresses` variable into a list of strings.

## Iterate through the remove list
Next, I needed to check a separate list called `remove_list` to see which IPs should be taken out of the `ip_addresses` list. I set up a `for` loop to iterate through every element in that list.

```python
# Iterate through each IP address in the remove list
for element in remove_list:
```

The `for`keyword starts the loop, and `element` serves as the loop variable. As the loop runs, `element` will represent each specific IP address in `remove_list` one by one.

## Remove IP addresses that are on the remove list
Inside the loop, I created a conditional statement to check if the current `element` (the IP to be removed) existed within the `ip_addresses` allow list. If it did, I used the `.remove()` method.

```python
# Check if the current element is in the allow list
    if element in ip_addresses:
        # Remove the IP address from the list
        ip_addresses.remove(element)
```

The `if` statement evaluates if the `element` is `in` the `ip_addresses` list. If the condition is true, `.remove(element)` is executed. This method is effective here because there are no duplicate IP addresses in the `ip_addresses` list; `.remove()` only deletes the first instance it finds, which is sufficient for this dataset.

## Update the file with the revised list of IP addresses

After cleaning the list, I needed to write the updated data back to the original file. To do this, I first converted the list back into a string using the `.join()` method, then opened the file in write mode.

```python
# Convert the list back into a string with new lines
ip_addresses = "\n".join(ip_addresses)

# Open the file in write mode and overwrite the contents
with open(import_file, "w") as file:
    file.write(ip_addresses)
```

I applied `.join()` to the `"\n"` (new line) character to ensure each IP address appears on its own line in the text file. Then, I used `with open(import_file, "w")` to open the file in **write** mode. The `"w"` argument is crucial because it tells Python to overwrite the existing contents of the file with the updated `ip_addresses` string using the `.write()` method.

## Summary
The algorithm successfully automates the management of an IP allow list by leveraging Python’s file handling and list manipulation capabilities. It begins by importing the text file and converting the contents into a list of strings for easy access. By iterating through a secondary "remove list," the script identifies and removes unauthorized access points using a conditional loop. Finally, the algorithm converts the refined list back into a string format and overwrites the original file with the current data. This process provides a reliable, repeatable method for maintaining security access lists without manual intervention