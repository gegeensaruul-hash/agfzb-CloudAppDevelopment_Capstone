import React, { useState } from 'react';
function Register() {
  const [username, setUsername] = useState('');
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const handleRegister = async (e) => {
    e.preventDefault();
    const response = await fetch('/djangoapp/registration', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ userName: username, firstName, lastName, email, password }),
    });
    const data = await response.json();
    if (data.status === 'Authenticated') {
      window.location.href = '/';
    } else {
      alert(data.error || 'Registration failed');
    }
  };
  return (
    <div>
      <h1>Sign Up</h1>
      <form onSubmit={handleRegister}>
        <input type="text" placeholder="Username" value={username} onChange={e => setUsername(e.target.value)} /><br/>
        <input type="text" placeholder="First Name" value={firstName} onChange={e => setFirstName(e.target.value)} /><br/>
        <input type="text" placeholder="Last Name" value={lastName} onChange={e => setLastName(e.target.value)} /><br/>
        <input type="email" placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} /><br/>
        <input type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} /><br/>
        <button type="submit">Register</button>
      </form>
    </div>
  );
}
export default Register;