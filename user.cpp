#include <iostream>
#include <string>

using namespace std;

int main(){

	string username ="";
	string password ="";
	bool loginSuccess =false;

	cout << "\tWelcome! Please Login below .\n\n";

	do{
	
	cout << "Username:    ";
	cin >> username;
	cout << "Password:    ";
	cin >> password;

	if (username == "Kenneth" && password == "ASDFGHJKL;'"){
		cout << "\nSuccessful Login\n\n";
		loginSuccess = true;
	}
	else if (username == "Alex" && password == "test"){
		cout << "\nSuccessful Login\n\n";
		loginSuccess = true;
		std::string filename = "/home/zeyuhe/Desktop/cs48_jocker/game.py";


std::string command = "python ";
command += filename;
system(command.c_str());

	}
	else{
		cout << "ID or password incorrect, please retry or contact our tech Ops manager Alex.\n";
	}

}while(!loginSuccess);

system("pause");
return 0;



}



