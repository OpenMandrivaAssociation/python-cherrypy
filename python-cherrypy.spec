%define tarname CherryPy-%{version}

Summary:        A Python-based framework for web application development
Name:           python-cherrypy
Version:        3.5.0
Release:        1
License:        BSD
Group:          Development/Python
URL:            http://www.cherrypy.org
Source0:        https://pypi.python.org/packages/source/C/CherryPy/CherryPy-%{version}.tar.gz
BuildRequires:	python-devel
BuildRequires:  python3-devel
BuildArch:      noarch

%description
A Python-based framework for web application development.

CheryPy allows you to write and easyly deploy web applications, thanks
to a bundled webserver. It features a automated way to map an url to a
mathod, allowing you to describe your site as a python class.

%package -n python3-cherrypy
Summary:        A Python-based framework for web application development
Group:          Development/Python
Requires:       python3
 
%description -n python3-cherrypy
A Python-based framework for web application development.

CheryPy allows you to write and easyly deploy web applications, thanks
to a bundled webserver. It features a automated way to map an url to a
mathod, allowing you to describe your site as a python class.

%prep
%setup -q -c

mv %{tarname} python2
cp -r python2 python3

%build
cat > tutorial.conf << EOF
[server]
socketPort = 8080
threadPool = 10

[session]
storageType=ram
EOF

pushd python2
cp ../tutorial.conf .
python setup.py build
popd

pushd python3
cp ../tutorial.conf .
%{__python3} setup.py build
popd

%install
pushd python3
%{__python3} setup.py install --root=%{buildroot} 
mv %{buildroot}/%{_bindir}/cherryd %{buildroot}/%{_bindir}/python3-cherryd
popd

pushd python2
python setup.py install --root=%{buildroot}
popd

%files -n python-cherrypy
%doc python2/README.txt
%doc python2/cherrypy/tutorial/*
%{py_puresitedir}/cherrypy/*
%{py_puresitedir}/*.egg-info
%{_bindir}/cherryd

%files -n python3-cherrypy
%doc python3/README.txt
%doc python3/cherrypy/tutorial/*
%{py3_puresitedir}/cherrypy/*
%{py3_puresitedir}/*.egg-info
%{_bindir}/python3-cherryd
