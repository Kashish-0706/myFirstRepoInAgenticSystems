# Role of query parameters in requests
Query parameters are used to filter and sort the data returned by API. In this request, **q= python** specifies the **search keyword**, **sort=stars and order=desc** ensure the results are **ranked by popularity**, and **per_page=5** limits the result size to the **top 5 matches**.


# Use of response.json() instead of response.text
**response.text** returns the raw content of the response as a **string**. **response.json()** is used because it automatically parses the JSON-formatted string into **Python dictionary** or list, making it much easier to access **specific data fields** like **"name"** or **"stargazers_count"** using **standard key-value indexing**.