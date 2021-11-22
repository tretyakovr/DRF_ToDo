import React from 'react';
import logo from './logo.svg';
import './App.css';
import './bootstrap.min.css'
import UsersList from './Components/Users.js'
import axios from 'axios'


class App extends React.Component {
   constructor(props) {
       super(props)
       this.state = {
           'users': []
       }
   }

componentDidMount() {
   axios.get('http://127.0.0.1:8000/api/users')
       .then(response => {
           const users = response.data
               this.setState(
               {
                   'users': users
               }
           )
       }).catch(error => console.log(error))
}


   render () {
       return (
            <div>
                <nav class="container navbar mb-4 sticky-top navbar-light bg-light">
                    Панель меню
                </nav>

                <div class="container" >
                    <UsersList users={this.state.users} />
                </div>

                <nav class="container navbar mt-4 fixed-bottom navbar-light bg-secondary text-light">
                    Footer
                </nav>
            </div>
       )
   }
}

export default App;
