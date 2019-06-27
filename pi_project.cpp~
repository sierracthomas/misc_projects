#include <iostream>
#include <ctime> //for time function                                            
#include <cstdlib> // for  random numbers                                       
#include <math.h> // for defining pi                                            
#include <random> // for random number generator                                
using namespace std;

int main(){
  //set up random number seed
  random_device rd;
  mt19937 gen(rd());
  uniform_real_distribution<> dis(0.0, 1.0);

  int number_darts = 100000000;

  //define darts thrown and darts that land in the circle                   
  int darts_thrown = 0;
  int in_circle = 0;
  
  while(darts_thrown < number_darts)
    {
      ++darts_thrown;
      double x = dis(gen);
      double y = dis(gen);

      if(x*x + y*y < 1)
	{
	  ++in_circle;
	}
    }
  // calculate pi                                          
  double pi_value = (in_circle * 4.0)/number_darts;
  cout << double (pi_value) << endl;
  

  return 0;

}
