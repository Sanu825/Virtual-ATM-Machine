<h1>ATM System README &#129297; &#129297;🏧</h1>

<p>This is a simple ATM (Automated Teller Machine) system implemented in Python. It allows users to check their balance, withdraw money, deposit money, and create new user accounts. The system stores user data in a JSON file.</p>

<h2>Features</h2>

<ol>
    <li><strong>User Authentication</strong>: Users can log in by entering their User ID and PIN. The system verifies the credentials to ensure the user's security.</li>
    <li><strong>Check Balance</strong>: Users can check their account balance.</li>
    <li><strong>Withdraw Money</strong>: Users can withdraw money from their account, provided they have a sufficient balance.</li>
    <li><strong>Deposit Money</strong>: Users can deposit money into their account.</li>
    <li><strong>Create New User</strong>: Users can create new accounts with unique User IDs, PINs, and initial balances.</li>
    <li><strong>Mini Statement</strong>: User can get their last 5 transaction very easily</li>
    <li><strong>User Data Storage</strong>: User data is stored in a JSON file, allowing for data persistence between program runs.</li>
</ol>

<h2>Installation and Setup</h2>

<ol>
    <li>Ensure you have Python installed on your system. You can download it from <a href="https://www.python.org/downloads/">python.org</a>.</li>
    <li>Clone or download this repository to your local machine.</li>
    <li>Install the required Python libraries, which are standard and should be available in your Python installation:
        <ul>
            <li><code>json</code>: For reading and writing user data to a JSON file.</li>
            <li><code>random</code>: For generating unique transaction IDs.</li>
        </ul>
    </li>
</ol>

<h2>Usage</h2>

<ol>
    <li>Run the <code>atm_system.py</code> script:
        <pre><code>python atm_system.py</code></pre>
    </li>
    <li>Follow the on-screen instructions to use the ATM system.</li>
    <li>You can perform actions such as checking your balance, withdrawing money, depositing money, or creating new user accounts.</li>
    <li>User data is stored in a <code>user_data.json</code> file and is loaded at the start of the program. Existing users are displayed, and you can perform transactions for these users.</li>
</ol>

<h2>User Data</h2>

<p>User data is stored in a JSON file named <code>user_data.json</code>. Each user entry consists of a User ID, a PIN, and an account balance. This file is automatically created if it doesn't exist.</p>

<h2>Contributing</h2>

<p>If you'd like to contribute to this project, please follow these guidelines:</p>

<ol>
    <li>Fork the repository.</li>
    <li>Make your changes or additions.</li>
    <li>Test your changes to ensure they work as expected.</li>
    <li>Create a pull request describing your changes and the problem or feature they address.</li>
</ol>

<h2>License</h2>

<p>This ATM System is open-source and available under the <a href="LICENSE">MIT License</a>. Feel free to use, modify, and distribute it as needed.</p>

<h2>Contact</h2>

<p>If you have any questions or issues, please feel free to contact the author:</p>

<p>Author: Sanu Kumar Das<br>
Email: dsanukumar90@gmail.com</p>

<p>Enjoy using the ATM System!</p>
