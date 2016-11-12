<template>
  <div class="card-ctr">
    <md-card v-for="i in [1,1,1,1,1,1,1]" md-with-hover>
      <md-card-header>
        <md-avatar>
          <img src="../assets/yoona.jpg" alt="People">
        </md-avatar>

        <div class="md-title">Title goes here</div>
        <div class="md-subhead">Subtitle here</div>
      </md-card-header>

      <md-card-media>
        <img src="../assets/yoona.jpg" alt="People">
      </md-card-media>

      <md-card-content>
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Optio itaque ea nostrum.
      </md-card-content>

      <md-card-actions>
        <md-button>Action</md-button>
        <md-button>Action</md-button>
      </md-card-actions>
    </md-card>
  </div>
</template>

<script>
export default {
  name: 'hello',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.card-ctr {
  margin: 0 auto;
  width: 1000px;
}
.md-card {
  display: inline-block;
  width: 240px;
  margin: 10px 5px;
}
.md-card-media {
  height: 200px;
  overflow: hidden;
}
</style>
