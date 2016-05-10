#include<iostream>
#include<mpi.h>
#include<stdio.h>
#include<stdlib.h>
#include <boost/algorithm/string/replace.hpp>
using namespace std;
int main(int argc, char **argv)
{
    MPI_Init(&argc, &argv);
    string cmd="";

    for(int cnt=1;cnt<argc;cnt++){
                cmd=cmd+" "+argv[cnt];
        }
    int local_rank;

    MPI_Comm_rank(MPI_COMM_WORLD,&local_rank);

    boost::replace_all(cmd,"@rank",to_string((long long)local_rank));

    system(cmd.c_str());

    MPI_Finalize();

}

