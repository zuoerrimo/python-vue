<template>
  <div id="app">
    <el-table
      :data="users"
      border
      stripe
      style="width: 100%">
      <el-table-column
        prop="id"
        label="编号"
        >
      </el-table-column>
      <el-table-column
        prop="name"
        label="姓名"
        >
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    name: 'App',
    data() {
      return {
        users: [],
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
    },
    mounted() {
      this.getUsers()
    }
  }
</script>

<style>
</style>
