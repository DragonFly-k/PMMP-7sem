using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GenerateScillet : MonoBehaviour
{
    public GameObject enemyPrefab;
    public Transform player;
    public Transform plane;
    public float visionAngle = 100f;
    public float visionDistance = 30f;
    public float movementSpeed = 3f;

    private List<GameObject> enemies = new List<GameObject>();

    void Start()
    {
        GenerateEnemies();

    }

    void Update()
    {
        DetectAndMoveTowardsPlayer();
    }

    void GenerateEnemies()
    {
        for (int i = 0; i < 10; i++)
        {
            float randomX = Random.Range(plane.TransformPoint(Vector3.left * plane.localScale.x / 2).x, plane.TransformPoint(Vector3.right * plane.localScale.x / 2).x);
            float randomZ = Random.Range(plane.TransformPoint(Vector3.back * plane.localScale.z / 2).z, plane.TransformPoint(Vector3.forward * plane.localScale.z / 2).z);

            Vector3 randomPosition = new Vector3(randomX, 1.25f, randomZ);

            Quaternion randomRotation = Quaternion.Euler(0, Random.Range(0, 360), 0);

            GameObject enemy = Instantiate(enemyPrefab, randomPosition, transform.rotation);


            enemies.Add(enemy);
        }
    }


    void DetectAndMoveTowardsPlayer()
    {
        foreach (var enemy in enemies)
        {
            Vector3 directionToPlayer = player.position - enemy.transform.position;

            float distanceToPlayer = directionToPlayer.magnitude;
            if (distanceToPlayer <= visionDistance)
            {
                float angleToPlayer = Vector3.Angle(enemy.transform.forward, directionToPlayer.normalized);

                if (angleToPlayer <= visionAngle * 0.5f)
                {
                    Quaternion lookRotation = Quaternion.LookRotation(directionToPlayer);
                    enemy.transform.rotation = Quaternion.Slerp(enemy.transform.rotation, lookRotation, Time.deltaTime * 5f);

                    enemy.transform.Translate(Vector3.forward * movementSpeed * Time.deltaTime);

                    if (distanceToPlayer <= 3f)
                    {
                        Debug.Log("YOU LOSE");
                        Destroy(player.gameObject);
                        player = null;
                    }
                }
            }
        }
    }

    public void DestroyEnemy(GameObject enemy)
    {
        if (enemies.Contains(enemy))
        {
            enemies.Remove(enemy);
            Destroy(enemy);
        }
        if (enemies.Count == 0)
        {
            print("YOU WIN");

        }

    }
}
