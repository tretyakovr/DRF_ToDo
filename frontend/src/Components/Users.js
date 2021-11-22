import React from 'react'


const UserItem = ({user}) => {
   return (
       <tr>
           <td>
               {user.username}
           </td>
           <td>
               {user.first_name}
           </td>
           <td>
               {user.last_name}
           </td>
           <td>
               {user.email}
           </td>
       </tr>
   )
}

const UsersList = ({users}) => {
   return (
       <table>
           <th>
               Логин
           </th>
           <th>
               Имя
           </th>
           <th>
               Фамилия
           </th>
           <th>
               email
           </th>
           {users.map((user) => <UserItem user={user} />)}
       </table>
   )
}


export default UsersList
