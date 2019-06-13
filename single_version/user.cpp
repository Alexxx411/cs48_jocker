#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main(int argc, char* argv[])
{
	if (argc != 3)
	{
		return -1;
	}
	string username, password;
	username = argv[1];
	password = argv[2];

	//then we search it to decide if we have the correspoding user info
	ifstream inFile;
	inFile.open("db.txt");

	if (!inFile)
	{
		cout << "Unable to open file" << endl;
		return -1;
	}

	int ret = 0;
	string _username, _password, _remain;
	while (getline(inFile, _username, ','))
	{
		// split to get username
		getline(inFile, _password, ',');

		// split to get password
		getline(inFile, _remain);
		if (username == _username)
		{
			ret = 1;
			if (password == _password)
			{
				ret = 2;
				break;
			}
		}
	}

	inFile.close();

	return ret;
}



