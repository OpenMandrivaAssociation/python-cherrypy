%define tarname CherryPy-%{version}

Summary:        A Python-based framework for web application development
Name:           python-cherrypy
Version:	18.10.0
Release:	2
License:        BSD
Group:          Development/Python
URL:            https://www.cherrypy.org
Source0:	https://files.pythonhosted.org/packages/source/C/CherryPy/cherrypy-%{version}.tar.gz
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(pip)
BuildArch:      noarch
%rename		python3-cherrypy
BuildSystem:	python

%description
A Python-based framework for web application development.

CheryPy allows you to write and easyly deploy web applications, thanks
to a bundled webserver. It features a automated way to map an url to a
mathod, allowing you to describe your site as a python class.

%prep -a
cat > tutorial.conf << EOF
[server]
socketPort = 8080
threadPool = 10

[session]
storageType=ram
EOF

%files -n python-cherrypy
%doc cherrypy/tutorial/*
%{python_sitelib}/cherrypy/*
%{python_sitelib}/*.*-info
%{_bindir}/cherryd
