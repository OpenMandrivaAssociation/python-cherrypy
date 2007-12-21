%define version 2.2.1
%define tarname CherryPy-%{version}


Summary:        A Python-based framework for web application development 
Name:           python-cherrypy
Version:        %version
Release:        %mkrel 1
Source0:        http://prdownloads.sourceforge.net/cherrypy/%tarname.tar.bz2
License:        BSD
Group:          Development/Python
URL:            http://www.cherrypy.org
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	python-devel
BuildArch:      noarch

%description
A Python-based framework for web application development. 

CheryPy allows you to write and easyly deploy web applications, thanks
to a bundled webserver. It features a automated way to map an url to a 
mathod, allowing you to describe your site as a python class.

%prep
%setup -q -n %tarname

%build
%__python setup.py build
cat > tutorial.conf << EOF
[server]
socketPort = 8080
threadPool = 10

[session]
storageType=ram
EOF

%install
%__rm -rf %buildroot
%__python setup.py install --root  %buildroot

%clean
%__rm -rf %buildroot

%files
%defattr(755,root,root)
%doc README.txt CHANGELOG.txt CHERRYPYTEAM.txt 
%doc cherrypy/tutorial/* 
%dir %{py_puresitedir}/cherrypy
%{py_puresitedir}/cherrypy/*
%{py_puresitedir}/*.egg-info


