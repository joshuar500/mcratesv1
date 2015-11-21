# mcratesv1

### 1st Time Usage
`git clone https://github.com/joshuar500/mcratesv1.git`
`cd mcratesv1`
`vagrant up`
`vagrant ssh`
`cd /vagrant/mcratesv1_project`
`mkvirtualenv mcrates`
`pip install django`
`pip install psycopg2`
`python manage.py migrate`
`python manage.py runserver 0.0.0.0:8000`

When you're done, `ctrl+d` to exit and `vagrant suspend` or `vagrant halt` to shutdown VM

### Next Time Usage
If you've already done the above
`vagrant up`
`vagrant ssh`
`workon mcrates`
`cd /vagrant/mcratesv1_project`
`python manage.py runserver 0.0.0.0:8000`
