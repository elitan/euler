#include <iostream>
#include <string>
#include <vector>
#include <stdlib.h>

using namespace std;

void add_one_to_vector(vector<int> & v, int index) {
	
	/*
	cout << "index: " << index << endl;

	cout << "vector before: ";
	for(int i = 0; i < v.size(); i++) {
		cout << v[i] << ", ";
	}
	cout << endl;
	*/

	if(index < 0) {
		cout << "exit" << endl;
		//exit(0);
		return;
	}

	int max_value = v.size();

	v[index]++;

	/*
	cout << "vector after: ";
	for(int i = 0; i < v.size(); i++) {
		cout << v[i] << ", ";
	}
	cout << endl;	

	cout << "check if " << v[index] << " > " << max_value << endl;
	*/
	if(v[index] > max_value) {
		v[index] = v[index-1]+1;
		add_one_to_vector(v, index-1);
	}

	/*
	cout << "#### START ####" << endl;

	for(int i = 0; i < v.size(); i++) {
		cout << v[i] << endl;
	}
	cout << "#### END ####" << endl;
	*/
}

int prod_of_vector(vector<int> v) {
	int s = 1;
	for(int i = 0; i < v.size(); i++)
		s *= v[i];
	return s;
}

int sum_of_vector(vector<int> v) {
	int s = 0;
	for(int i = 0; i < v.size(); i++)
		s += v[i];
	return s;
}

int main() {

	int side_sum = 0;
	int side_prod = 0;
	int k = 2;

	while(1) {
		side_sum = k;
		vector<int> prod_v (k, 1);
		side_prod = prod_of_vector(prod_v);

		while(side_sum != side_prod) {

			cout << "did not work, next number..." << endl;


			cout << "#### START ####" << endl;

			for(int i = 0; i < prod_v.size(); i++) {
				cout << prod_v[i] << endl;
			}
			cout << "#### END ####" << endl;			
			// add one to vector
			add_one_to_vector(prod_v, prod_v.size()-1);
			cout << "#### START ####" << endl;

			for(int i = 0; i < prod_v.size(); i++) {
				cout << prod_v[i] << endl;
			}
			side_prod = prod_of_vector(prod_v);
			side_sum = sum_of_vector(prod_v);
		}

		cout << "k: " << k << ", " << side_sum << endl;

		k++;
		if(k == 6)
			exit(0);
	}
}