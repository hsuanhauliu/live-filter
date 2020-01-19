# Live Filter

A tool that allows you to experiment with image filters.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Dependencies

See [here](requirements.txt) for a complete list of required packages.
- Python >= 3.7.4
- Flask >= 1.1.1
- OpenCV >= 4.1.1.26
- Numpy >= 1.17.3

### Installation

A step by step series of examples that tell you how to get a development env running.

Use the following command to install all packages.
```bash
pip install -r requirements.txt
```

### Usage

To start the program, enter command

```bash
python3 live-filter
```

Once the server is up and running, type http://0.0.0.0:8000 in your web browser.

### Custom Filters

To implement your own custom filters, follow the steps below.

1. In the templates/index.html file, add a new button for the custom filter by copying and pasting an input tag nested inside of the "Filter control panel" div tag. The value of the tag will be used to identify the class of the filter that you'll be creating.

```html
<input type="submit" name="filter_button" value="new_filter_id"/>
```

2. Implement your custom filter in the filters/ directory. Follow the same pattern as other filters to implement the new filter. The apply function is what the program will execute once button is pressed.

```python
from live_filter.filters.filter import Filter

class NewFilter(Filter):
    
    def apply(self, im):
        # your implementation
```

3. In liver_filter.filters.__init__.py file, add your Filter for importing.

```python
from live_filter.filters.new_filter import NewFilter
```

4. Finally, go to filter_manager.py filter, add a new key and value pair to the filter_dict dictionary inside of the FilterManager class. The new key must match the value that you've given to the new button in step one. The value pair is a function call to the constructor of the new class that you've just created.

```python
filter_dict = {
    ...
    "new_filter_id": fil.NewFilter()
}
```