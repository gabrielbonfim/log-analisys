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
- Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads). You do not need to launch VirtualBox after installing it.
- Install [Vagrant](https://www.vagrantup.com/downloads.html). Vagrant is the program that will download a Linux operating system and run it inside the virtual machine.
- Fork the [VM configuration](https://github.com/udacity/fullstack-nanodegree-vm). `cd` into the "vagrant" directory and execute `vagrant up`. This will copy (in the first run) and start the virtual machine. Once started access the virtual machine via SSH with `vagrant ssh` (password is vagrant). 
- Download (wget) [Database data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Extract with `unzip newsdata.zip`. Import the sql file to the database with `psql -d news -f newsdata.sql`.
- [Python](https://www.python.org/) - Already installed in the virtual machine
- [PostgreSQL](https://www.postgresql.org/) - Already installed in the virtual machine

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