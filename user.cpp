#include <iostream>
#include <string>
#include <fstream>


using namespace std;

int main() {

	string username = "";
	string password = "";

	string new_name = "";
	string new_password = "";


	bool loginSuccess = false;



	cout << "\tWelcome! Please Login below .\n\n";

	do {

		cout << "Username:    ";
		cin >> username;
		cout << "Password:    ";
		cin >> password;

//then we search it to decide if we have the correspoding user info
		ifstream inFile;
		string line;

		inFile.open("account.txt");

		if (!inFile) {
			cout << "Unable to open file" << endl;
			exit(1);
		}

		string search = username;

		size_t pos ;
		size_t pos2;
		int line_pos = 0;

		while (inFile.good())
		{
			getline(inFile, line); // get line from file
			pos = line.find(search); // search
			pos2 = line.find(password);
			if (pos != string::npos && pos2 != string::npos) // string::npos is returned if string is not found
			{
				// cout<<"find!"<<endl;
				// string correct = "";
				// getline(inFile,line2);
				// if ( line2 == password)
				// {
				loginSuccess = true;
				// }
				//  if we have the user passed the log in password, we will store the line of this
				//  user in the very last line
				std::ofstream outfile;
				outfile.open("account.txt", std::ios_base::app);
				outfile << line_pos << endl;

				break;
			}
			line_pos++;
		}
		if (username == "Kenneth" && password == "ASDFGHJKL;'") {
			cout << "\nSuccessful Login\n\n";
			loginSuccess = true;
		}
		else if (username == "Alex" && password == "test") {
			cout << "\nSuccessful Login\n\n";
			loginSuccess = true;



		}
		else if (username == "create" ) {
			loginSuccess = true;
			// 	cout<<"New username: ";
			// 	cin >> new_name;
			// 	cout<<"New password: ";
			// 	cin >> new_password;
			// 	std::ofstream outfile ("account.txt");
			// 	//here we store the new user name and new user password
			// outfile  << new_name<< std::endl;
			// outfile  << new_password<<std::endl;
			// outfile.close();

			// ofstream myfile;
//  myfile.open ("account.txt");
			cout << "New username: ";
			cin >> new_name;
			cout << "New password: ";
			cin >> new_password;

			std::ofstream outfile;
			outfile.open("account.txt", std::ios_base::app);
			outfile << new_name << " " << new_password << " " << 1000 << endl;
			outfile.close();

			// then we search again
			string search = new_name;

			size_t pos ;
			size_t pos2;
			int line_pos = 0;
			// cout<<"ya0";
			inFile.close();
			inFile.open("account.txt");
			while (inFile.good())
			{
				// cout<<"ya";
				getline(inFile, line); // get line from file
				pos = line.find(search); // search
				pos2 = line.find(new_password);
				if (pos != string::npos && pos2 != string::npos) // string::npos is returned if string is not found
				{
					// cout<<"find!"<<endl;
					// string correct = "";
					// getline(inFile,line2);
					// if ( line2 == password)
					// {
					loginSuccess = true;
					// cout<<"ya!";
					// }
					//  if we have the user passed the log in password, we will store the line of this
					//  user in the very last line
					std::ofstream outfile;
					outfile.open("account.txt", std::ios_base::app);
					outfile << line_pos << endl;

					break;
				}
				line_pos++;
			}


		}
		if (loginSuccess == true)
		{
			std::string filename = "/home/zeyuhe/Desktop/cs48_jocker/verision5_16/cs48_jocker-master/game.py";

			std::string command = "python ";
			command += filename;
			system(command.c_str());
		}
		else {
			cout << "ID or password incorrect, please retry or contact our tech Ops manager Alex. If you want to create a new account. enter create\n";
		}







	}
	while (!loginSuccess);

	system("");
	return 0;



}



