# Logs Analysis
Reporting tool that prints out reports in plain text based on the data in the database "news"

Reports:
1) The most popular three articles of all time
2) The most popular article authors of all time
3) Days with more than 1% of requests that lead to errors

## [Project Files](https://github.com/gabrielbonfim/movie-trailer-website)
- `log-analysis.py` - Module that displays the reports results
- `LICENSE` - The license associated with this project
- `README.md` - This file

## Getting Started
### Prerequisites
[Python](https://www.python.org/)
[PostgreSQL](https://www.postgresql.org/)
(Both are installed in the Udacity virtual machine for this course)

** Important - View creation **

create view articles_top_desc as select path, substr(path,10,length(path)) as slug, count(*) as count from log where path like '%/article/%' and status like '200 OK' group by path order by count desc;

### Installing
```
git clone https://github.com/gabrielbonfim/log-analysis
```

### Usage
```
cd log-analysis
python log-analysis.py
```
### Enjoy
&#128526;

## Build With
[Visual Studio Code](https://code.visualstudio.com/)

## Author
[Gabriel Almeida](https://www.linkedin.com/in/gabriel-bonfim-almeida/) (Udacity Student)

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/gabrielbonfim/movie-trailer-website/blob/master/LICENSE) file for details