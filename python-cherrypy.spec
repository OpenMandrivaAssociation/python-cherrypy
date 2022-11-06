%define tarname CherryPy-%{version}

Summary:        A Python-based framework for web application development
Name:           python-cherrypy
Version:	18.8.0
Release:	1
License:        BSD
Group:          Development/Python
URL:            http://www.cherrypy.org
Source0:	https://files.pythonhosted.org/packages/source/C/CherryPy/CherryPy-%{version}.tar.gz
BuildRequires:  python3-devel
BuildRequires:  python-setuptools
BuildArch:      noarch
%rename		python3-cherrypy

%description
A Python-based framework for web application development.

CheryPy allows you to write and easyly deploy web applications, thanks
to a bundled webserver. It features a automated way to map an url to a
mathod, allowing you to describe your site as a python class.

%prep
%autosetup -p1 -n CherryPy-%{version}

%build
cat > tutorial.conf << EOF
[server]
socketPort = 8080
threadPool = 10

[session]
storageType=ram
EOF

%py_build

%install
%py_install

%files -n python-cherrypy
%doc cherrypy/tutorial/*
%{python_sitelib}/cherrypy/*
%{python_sitelib}/*.egg-info
%{_bindir}/cherryd
