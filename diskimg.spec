Summary:	A tools to make disks/partitions image
Name:		diskimg
Version:	1.1.1
Release:	10
License:	GPL
Group:		Archiving/Backup
Url:		http://www.scylla-charybdis.com/tools.html#diskimg
Source0:	%{name}.tar.bz2

%description
DiskImg is a small command-line utility that dumps the contents
of a drive or partition to standard out. Because it is based on 
large file support, it is able to skip over read errors and log
them to a log file. It can start reading at an offset and writes
its progress to stderr.

%files
%doc VERSION README
%{_bindir}/%{name}

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%make "CFLAGS=%{optflags}"

%install
install -D %{name} %{buildroot}%{_bindir}/%{name}

