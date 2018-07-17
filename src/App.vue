<template>
  <div id="app">
    <el-table
      :data="users"
      style="width: 100%">
      <el-table-column
        prop="id"
        label="编号"
        width="180">
      </el-table-column>
      <el-table-column
        prop="name"
        label="姓名"
        width="180">
      </el-table-column>
    </el-table>
    {{msg}}
  </div>
</template>

<script>
  import axios from 'axios'
  import _ from 'lodash'
  export default {
    name: 'App',
    data() {
      return {
        users: [],
        msg: '',
      }
    },
    methods: {
      getUsers() {
        axios
        .get('http://127.0.0.1:5000/userList')
        .then((res) => {
          this.users = res.data.users.map((user) => {
            return {
              id: user[0],
              name: user[1]
            }
          })
        })
      },
      getMsg() {
        axios
        .get('http://127.0.0.1:5000/getMsg')
        .then((res) => {
          this.msg = res.data.msg
        })
      },
    },
    mounted() {
      this.getMsg()
      this.getUsers()
    }
  }
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
