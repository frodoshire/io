<template>
  <b-container fluid>
    <div class="d-inline-flex p-2">
      <b-form-input v-model="msg" placeholder="URL"></b-form-input>
    </div>
    <div class="d-inline-flex p-2">
      <b-button block variant="primary" v-on:click="myfun">Short</b-button>
    </div>
    <p>{{ msg1 }}</p>
  </b-container>
</template>

<script>
export default {
  name: "HelloWorld",
  data() {
    return {
      msg: "",
      msg1: ""
    };
  },
  methods: {
    myfun() {
      this.axios
        .post("http://localhost:8000/shortener", {
          url: this.msg
        })
        // .then(response => console.log(response.data));
        .then(
          response => (this.msg1 = window.location.pathname + response.data.url)
        )
        .catch(error => {
          console.log(error);
          this.msg1 = error;
        });
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
